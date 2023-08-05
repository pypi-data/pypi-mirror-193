//
// This file auto-generated with generate-wrappers.js
//

var _ = require('underscore');
var Promise = require('bluebird');
var THREE = require('three');
var widgets = require('@jupyter-widgets/base');
var dataserializers = require('jupyter-dataserializers');
var serializers = require('../_base/serializers');

var BaseBufferGeometryModel = require('../core/BaseBufferGeometry.autogen.js').BaseBufferGeometryModel;


class TorusBufferGeometryModel extends BaseBufferGeometryModel {

    defaults() {
        return _.extend(BaseBufferGeometryModel.prototype.defaults.call(this), {

            radius: 1,
            tube: 0.4,
            radialSegments: 8,
            tubularSegments: 6,
            arc: 6.283185307179586,
            type: "TorusBufferGeometry",

        });
    }

    constructThreeObject() {

        var result = new THREE.TorusBufferGeometry(
            this.convertFloatModelToThree(this.get('radius'), 'radius'),
            this.convertFloatModelToThree(this.get('tube'), 'tube'),
            this.get('radialSegments'),
            this.get('tubularSegments'),
            this.convertFloatModelToThree(this.get('arc'), 'arc')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        BaseBufferGeometryModel.prototype.createPropertiesArrays.call(this);

        this.props_created_by_three['type'] = true;

        this.property_converters['radius'] = 'convertFloat';
        this.property_converters['tube'] = 'convertFloat';
        this.property_converters['radialSegments'] = null;
        this.property_converters['tubularSegments'] = null;
        this.property_converters['arc'] = 'convertFloat';
        this.property_converters['type'] = null;


    }
}

TorusBufferGeometryModel.model_name = 'TorusBufferGeometryModel';
TorusBufferGeometryModel.serializers = {
    ...BaseBufferGeometryModel.serializers,
};

module.exports = {
    TorusBufferGeometryModel: TorusBufferGeometryModel,
};
