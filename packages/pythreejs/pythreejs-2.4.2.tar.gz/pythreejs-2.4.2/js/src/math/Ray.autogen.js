//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var ThreeModel = require('../_base/Three.js').ThreeModel;


class RayModel extends ThreeModel {

    defaults() {
        return _.extend(ThreeModel.prototype.defaults.call(this), {

            origin: [0,0,0],
            direction: [0,0,0],

        });
    }

    constructThreeObject() {

        var result = new THREE.Ray(
            this.convertVectorModelToThree(this.get('origin'), 'origin'),
            this.convertVectorModelToThree(this.get('direction'), 'direction')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        ThreeModel.prototype.createPropertiesArrays.call(this);


        this.property_converters['origin'] = 'convertVector';
        this.property_converters['direction'] = 'convertVector';

        this.property_assigners['origin'] = 'assignVector';
        this.property_assigners['direction'] = 'assignVector';

    }
}

RayModel.model_name = 'RayModel';
RayModel.serializers = {
    ...ThreeModel.serializers,
};

module.exports = {
    RayModel: RayModel,
};
