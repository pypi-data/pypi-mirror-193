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


class TorusKnotBufferGeometryModel extends BaseBufferGeometryModel {

    defaults() {
        return _.extend(BaseBufferGeometryModel.prototype.defaults.call(this), {

            radius: 1,
            tube: 0.4,
            tubularSegments: 64,
            radialSegments: 8,
            p: 2,
            q: 3,
            type: "TorusKnotBufferGeometry",

        });
    }

    constructThreeObject() {

        var result = new THREE.TorusKnotBufferGeometry(
            this.convertFloatModelToThree(this.get('radius'), 'radius'),
            this.convertFloatModelToThree(this.get('tube'), 'tube'),
            this.get('tubularSegments'),
            this.get('radialSegments'),
            this.get('p'),
            this.get('q')
        );
        return Promise.resolve(result);

    }

    createPropertiesArrays() {

        BaseBufferGeometryModel.prototype.createPropertiesArrays.call(this);

        this.props_created_by_three['type'] = true;

        this.property_converters['radius'] = 'convertFloat';
        this.property_converters['tube'] = 'convertFloat';
        this.property_converters['tubularSegments'] = null;
        this.property_converters['radialSegments'] = null;
        this.property_converters['p'] = null;
        this.property_converters['q'] = null;
        this.property_converters['type'] = null;


    }
}

TorusKnotBufferGeometryModel.model_name = 'TorusKnotBufferGeometryModel';
TorusKnotBufferGeometryModel.serializers = {
    ...BaseBufferGeometryModel.serializers,
};

module.exports = {
    TorusKnotBufferGeometryModel: TorusKnotBufferGeometryModel,
};
