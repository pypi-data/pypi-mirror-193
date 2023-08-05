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


class FogModel extends ThreeModel {

    defaults() {
        return _.extend(ThreeModel.prototype.defaults.call(this), {

            name: "",
            color: "white",
            near: 1,
            far: 1000,

        });
    }

    constructThreeObject() {

        var result = new THREE.Fog(
            this.convertColorModelToThree(this.get('color'), 'color'),
            this.convertFloatModelToThree(this.get('near'), 'near'),
            this.convertFloatModelToThree(this.get('far'), 'far')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        ThreeModel.prototype.createPropertiesArrays.call(this);


        this.property_converters['name'] = null;
        this.property_converters['color'] = 'convertColor';
        this.property_converters['near'] = 'convertFloat';
        this.property_converters['far'] = 'convertFloat';


    }
}

FogModel.model_name = 'FogModel';
FogModel.serializers = {
    ...ThreeModel.serializers,
};

module.exports = {
    FogModel: FogModel,
};
